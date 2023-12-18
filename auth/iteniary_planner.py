from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import tensorflow as tf

def iteniary_model (user_id, city) :
    model=load_model('./Model/iteniary_model')
    
    user_pilih = user_id
    kota_terpilih = city

    # Import Data
    rating = pd.read_csv('./Model/dataset/tourism_rating.csv')
    place = pd.read_csv('./Model/dataset/tourism_with_id.csv')
    user = pd.read_csv('./Model/dataset/user.csv')

    #Merge Data
    rating = pd.merge(rating, place[['Place_Id']], how='right', on='Place_Id')
    user = pd.merge(user, rating[['User_Id']], how='right', on='User_Id').drop_duplicates().sort_values('User_Id')
    place = pd.read_csv('./Model/dataset/tourism_with_id.csv')
    place = place.drop(['Unnamed: 11','Unnamed: 12'],axis=1)

    place_df = place[['Place_Id','Place_Name','Category','Rating','Price']]
    place_df.columns = ['id','place_name','category','rating','price']


    place = place[place['City'].isin([kota_terpilih])]

    df=rating.copy()
    user_unique_vals = df['User_Id'].unique().tolist()
    user_to_user_encoded = {x: i for i, x in enumerate(user_unique_vals)}
    user_encoded_to_user = {i: x for i, x in enumerate(user_unique_vals)}
    df['user'] = df['User_Id'].map(user_to_user_encoded)

    place_unique_vals = df['Place_Id'].unique().tolist()
    place_to_place_encoded = {x: i for i, x in enumerate(place_unique_vals)}
    place_encoded_to_place = {i: x for i, x in enumerate(place_unique_vals)}
    df['place'] = df['Place_Id'].map(place_to_place_encoded)

    # Mendapatkan jumlah user dan place
    num_users, num_place = len(user_to_user_encoded), len(place_to_place_encoded)

    # Mengubah rating menjadi nilai float
    df['Place_Ratings'] = df['Place_Ratings'].values.astype(np.float32)

    # Mendapatkan nilai minimum dan maksimum rating
    min_rating, max_rating = min(df['Place_Ratings']), max(df['Place_Ratings'])

    # print(f'Number of User: {num_users}, Number of Place: {num_place}, Min Rating: {min_rating}, Max Rating: {max_rating}')

    place_df = place[['Place_Id','Place_Name','Category','Rating','Price']]
    place_df.columns = ['id','place_name','category','rating','price']
    df = rating.copy()

    #enconding
    user_id = user_pilih
    place_visited_by_user = df[df.User_Id == user_id]

    # Membuat data lokasi yang belum dikunjungi user
    place_not_visited = place_df[~place_df['id'].isin(place_visited_by_user.Place_Id.values)]['id']
    place_not_visited = list(
        set(place_not_visited)
        .intersection(set(place_to_place_encoded.keys()))
    )

    place_not_visited = [[place_to_place_encoded.get(x)] for x in place_not_visited]
    user_encoder = user_to_user_encoded.get(user_id)
    user_place_array = np.hstack(
        ([[user_encoder]] * len(place_not_visited), place_not_visited)
    )

    # Mengambil top 7 recommendation
    user_place_array = tf.cast(user_place_array, tf.int64)
    ratings = model.predict(user_place_array).flatten()

    top_ratings_indices = ratings.argsort()[-len(ratings):][::-1]
    recommended_place_ids = [
        place_encoded_to_place.get(place_not_visited[x][0]) for x in top_ratings_indices
    ]

    top_place_user = (
        place_visited_by_user.sort_values(
            by='Place_Ratings',
            ascending=False
        )
        .head(10)
        .Place_Id.values
    )

    place_df_rows = place_df[place_df['id'].isin(top_place_user)]
    # for row in place_df_rows.itertuples():
    #    print(row.place_name, ':', row.category)

    recommended_place = place_df[place_df['id'].isin(recommended_place_ids)]
    return recommended_place


def filterin_iteniary(df, n_days, max_budget):
    df = df.reset_index()
    iteniary_df = pd.DataFrame()
    total_cost = 0
    max_places = n_days * 4

    for i in range(len(df)):
        price = int(df.loc[i]['price'])

        if total_cost + price > max_budget:
            break

        total_cost += price

        place = pd.DataFrame({'place_name': [df.loc[i, 'place_name']], 'price': [price], 'category': [df.loc[i, 'category']], 'rating': [df.loc[i, 'rating']]})
        iteniary_df = pd.concat([iteniary_df, place])

        if len(iteniary_df) == max_places:
            break
    
    # Assign day values
    iteniary_df['day'] = [((i // 4) + 1) for i in range(len(iteniary_df))]

    return iteniary_df

def iteniary_planner(user_id, city, n_days, max_budget):
    place_prediction = iteniary_model(user_id, city)
    final_iteniary = filterin_iteniary(place_prediction, n_days, max_budget)
    return final_iteniary

def print_itinerary(df_iteniary):
    # Define time slots
    time_slots = ['09:00 - 11:00', '11:00 - 13:00', '13:00 - 15:00', '15:00 - 17:00']

    # Get unique days
    days = df_iteniary['day'].unique()

    for day in days:
        # Print day header
        print("======================")
        print(f"                    Day {day}")
        print("======================\n")

        # Filter activities for the day
        day_activities = df_iteniary[df_iteniary['day'] == day]

        for i, (index, row) in enumerate(day_activities.iterrows()):
            # Get time slot
            time_slot = time_slots[i % 4]

            # Print activity details
            print(f"{time_slot}: {row['place_name']} (Price: {row['price']}) (Category: {row['category']}) (Rating: {row['rating']})")

        # Print a newline for separation between days
        print("\n")

