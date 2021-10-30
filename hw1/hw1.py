#Edit on 7:17pm
#TASK 1: READING DATA

#1) Write a function read_ratings_data(f) that takes in a ratings file, and returns a dictionary. The dictionary should have movie as key, and the corresponding list of ratings as value.

def read_ratings_data(f):
    dict_output = {}
    
    for each_line in open(f):   #read one line at a time
        current_line = each_line.split("|")  #returns list
        movie_name = current_line[0].strip()
        rating = float(current_line[1])
        
        if movie_name in dict_output: #if movie is already in dictionary
            dict_output[movie_name].append(rating)
        else: #if movie not in dictionary
            dict_output[movie_name] = [rating]
    print dict_output
    return dict_output

#2) Write a function read_movie_genre(f) that takes in a movies file and returns a dictionary. The dictionary should have a one-to-one mapping between movie and genre.

def read_movie_genre(f):
    output_dict = {}
    
    for each_line in open(f): #read one line at a time
        current_line = each_line.split("|") #returns list
        genre = current_line[0].strip()
        movie_name = current_line[2].strip()
        
        if movie_name in output_dict:
            continue
        else:
            output_dict[movie_name] = genre
        
    return output_dict

# Possibly more efficient
#def read_rating_data(f):
    #output_dict = {}
    #for line in open(f):
        #genre, movie_ID, movie_name = line.split('|')
        #genreDataDict[movie_name.strip()] = genre.strip()
    #print(genreMovieDict)
    #return(output_dict)

#All methods in task 1 work


#TASK 2: PROCESSING DATA

#1) Genre dictionary Write a function create_genre_dict that takes as a parameter a movie-to-genre dictionary, of the kind created in Task 1.2. The function should return another dictionary in which a genre is mapped to all the movies in that genre.

def create_genre_dict(movie_to_genre_dict):
    dict_output = {}
    
    for key in movie_to_genre_dict:
        movie = key
        genre = movie_to_genre_dict[key]
        
        if genre in dict_output:
            dict_output[genre].append(movie)
        else: #genre hasnt been added yet
            dict_output[genre] = [movie]
            
    return dict_output


#2 Average Rating Write a function calculate_average_rating that takes as a parameter a ratings dictionary, of the kind created in Task 1.1. It should return a dictionary where the movie is mapped to its average rating computed from the ratings list.

def calculate_average_rating(ratings_dict):
    dict_output = {}
    
    for key in ratings_dict: #iterates thru every key 
        movie = key
        average_rating = sum(ratings_dict[key]) / len(ratings_dict[key])
        
        dict_output[key] = average_rating
        
    return dict_output



#TASK 3: RECOMMENDATION

#1 Populartiy Based 
# Write a function get_popular_movies that takes as parameters a dictionary of movie-to-average rating ( as created in Task 2.2), and an integer n (default should be 10). The function should return a dictionary ( movie:average rating, same structure as input dictionary) of top n movies based on the average ratings. (If there are fewer movies than n, it should all return all movies in order of top average ratings.)

def get_popular_movies(dict_movie_to_avg_rating, n = 10):
    output_dict = {}
    
    #sort movie avg rating list
    dict_movie_to_avg_rating_sorted_list = sorted(dict_movie_to_avg_rating.items(), reverse = True, key = lambda movie: movie[1]) #returns sorted list based on rating
    
    for i in range(n): #0, 1, 2, ... n - 1
        try:
            movie = dict_movie_to_avg_rating_sorted_list[i][0]
            avg_rating = dict_movie_to_avg_rating_sorted_list[i][1]
            output_dict[movie] = avg_rating
        except: #ie.g. if there's 5 movies and n = 10
            break 

            
    return output_dict


#2 Threshold Rating
# Write a function filter_movies that takes as parameters a dictionary of movie-to-average rating (same as for the popularity based function above), and a threshold rating with default value of 3. The function should filter movies based on the threshold rating, and return a dictionary with same structure as the input. For example, if the threshold rating is 3.5, the returned dictionary should have only those movies from the input whose average rating is equal to or greater than 3.5.

def filter_movies(dict_of_movie_to_avg_rating, threshold_rating = 3):
    output_dict = {} #return a dictionary w/ same structure as the input (dictionary of movie to average rating)
    
    for key in dict_of_movie_to_avg_rating: #iterates thru every key
        if dict_of_movie_to_avg_rating[key] >= threshold_rating:
            output_dict[key] = dict_of_movie_to_avg_rating[key]
            
    return output_dict

    


#3 Popularity + Genre based
#Write a function get_popular_in_genre that, given a genre, a genre-to-movies dictionary (as created in Task 2.1), a dictionary of movie:average rating (as created in Task 2.2), and an integer n (default 5), returns the top n most popular movies in that genre based on the average ratings. The return value should be a dictionary of movie-to-average rating of movies that make the cut. Genre categories will be from those in the movie:genre dictionary created in Task 1.2. Your code should handle the case when there are fewer than n movies in the data, as in Task 3.1 above.

def get_popular_in_genre(genre, genre_to_movies_dict, movie_average_rating_dict, n = 5):
    
    output_dict = {} #return top n most popular movies in that genre based on avg ratings. Return: dict of movie to avg rating that make the cut
    
    
    list_of_movies_of_genre = genre_to_movies_dict[genre] #get list of movies of given genre
    

    dict_movies_genre_rating = {} #dictionary of movies of given genre and corresponding avg ratings
    
    for movie in list_of_movies_of_genre: #iterate thru list of movies of given genre
        dict_movies_genre_rating[movie] = movie_average_rating_dict[movie]
        
    dict_movies_genre_rating_sorted_list = sorted(dict_movies_genre_rating.items(), reverse = True, key = lambda movie: movie[1])  #sorting the dict of movies of genre based on avg rating

    for i in range(n): #0, 1, 2, ... (n-1)
        try:
            movie = dict_movies_genre_rating_sorted_list[i][0]
            avg_rating = dict_movies_genre_rating_sorted_list[i][1]
            output_dict[movie] = avg_rating
        except:
            break
            
    return output_dict


#4 Genre Rating
#Write a function get_genre_rating that takes the same parameters as get_popular_in_genre above, except for n, and returns the average rating of the movies in the given genre.

#return single number
#calculalte the average of the average using movie to avg rating
def get_genre_rating(genre, genre_to_movie_dict, movie_avg_rating_dict):
    output_dict = {}
    list_of_movies_of_genre = genre_to_movie_dict[genre] # list of all movies of given genre
    
    for movie in list_of_movies_of_genre: #for each movie of genre in list
        output_dict[movie] = movie_avg_rating_dict[movie]
        
    #return avg rating of movies in given genre
    sum_Rating = 0
    numbOfMovies = 0;
    for key in output_dict:
        sum_Rating = sum_Rating + output_dict[key]
        numbOfMovies = numbOfMovies + 1
        
    return sum_Rating / numbOfMovies
    




#5 Genre Popularity
# Write a function genre_popularity that takes as parameters a genre-to-movies dictionary (as created in Task 2.1), a movie-to-average rating dictionary (as created in Task 2.2), and n (default 5), and returns the top-n rated genres as a dictionary of genre:average rating. Hint: Use the above get_genre_rating function as a helper

    #take the average of the average rating. Same thing mathematically as addding each individual ratings(not avg) and dividing by amount of #s
    
    #in genre:average rating dictionary, what does average rating refer to? How to calculate it? Need to use get_genre_rating fuction?
        
    # (Make sure to test your programs on files other than the samples we have provided, to cover the various paths of logic in your code.) WHAT DOES THIS MEAN?
    
def genre_popularity(genre_to_movies_dict, movie_avg_rating_dict, n = 5):
    output_dict = {} #returns dictionary genre: avg rating
    
    for each_genre in genre_to_movies_dict:
        output_dict[each_genre] = get_genre_rating(each_genre, genre_to_movies_dict, movie_avg_rating_dict) #returns  avg rating of movies in this genre (single number)
    
    #sort the dictionary and  return top n
    output_dict2 = {} #same as output_dict but has it in reverse order
    output_dict_sorted_list = sorted(output_dict.items(), reverse = True, key = lambda rating: rating[1])
    for i in range(n):
        genre = output_dict_sorted_list[i][0]
        genre_rating = output_dict_sorted_list[i][1]
        output_dict2[genre] = genre_rating
    
    return output_dict2
    
    
    
    
    
    
#TASK 4 (USER FOCUSED)

#1) Read the ratings file to return a user-to-movies dictionary that maps user ID to the associated movies and the corresponding ratings. Write a function named read_user_ratings for this, with the ratings file as the parameter.

def read_user_ratings(f):
    output_dict = {}
    
    for each_line in open(f): # read one line at a time
        
        current_line = each_line.split("|") #returns list
        movie = current_line[0]
        rating = float(current_line[1])
        userID = int(current_line[2])
        
        if userID in output_dict:
            tuple_to_append = (movie, rating)
            output_dict[userID].append(tuple_to_append)
        else:
            output_dict[userID] = [(movie, rating)]
        
    return output_dict



#2
#Write a function get_user_genre that takes as parameters a user id, the user-to-movies dictionary (as created in Task 4.1 above), and the movie-to-genre dictionary (as created in Task 1.2), and returns the top genre that the user likes based on the user's ratings. Here, the top genre for the user will be determined by taking the average rating of the movies genre-wise that the user has rated.

#WHAT TO RETURN IF USER RATED 3 MOVIES THE SAME THAT ARE ALL OF DIFFERENTE GENRE
#Return any genre if theres a tie

def get_user_genre(userID, user_to_movies_dict, movie_to_genre_dict): #Returns top genre of user
    movies_rating_tuple_of_user_list = user_to_movies_dict[userID] #gets all movies and corresponding rating that user rated
    helper_dict = {} #genre: [sum rating, numbOfRatings] dictionary. USE THIS TO GET AVG RATING OF MOVIES GENRE WISE
    
    for each_tuple in movies_rating_tuple_of_user_list: #for each (movie, rating) in list
        movie = each_tuple[0]
        rating = each_tuple[1]
        genre = movie_to_genre_dict[movie]
        try:
            helper_dict[genre][0] =  helper_dict[genre][0] + rating #adding rating to sum
            helper_dict[genre][1] =  helper_dict[genre][1] + 1 #updating number of ratings
        except: #If its first time adding genre
            helper_dict[genre] = [rating, 1]
            
    #using helper_dict, calculate avg and append it to the end of each list in dictionary
    for genre in helper_dict:
        helper_dict[genre].append(helper_dict[genre][0] / helper_dict[genre][1]) #now dict is of form... genre:[sum rating, # of ratings, avg rating]
    
    #sorting by avg rating
    helper_dict_sorted_list = sorted(helper_dict.items(), reverse = True, key = lambda avgRating: avgRating[1][2])
        
    top_genre_of_user = helper_dict_sorted_list[0][0]
    return top_genre_of_user


    


    
#3 Recommend 3 most popular (highest average rating) movies from the user's top genre that the user has not yet rated. Write a function recommend_movies for this, that takes a parameters a user id, the user-to-movies dictionary (as created in Task 4.1 above), the movie-to-genre dictionary (as created in Task 1.2), and the movie-to-average rating dictionary (as created in Task 2.2). The function should return a dictionary of movie-to-average rating. (Return all if fewer than 3 movies make the cut.)

def recommend_movies(userID, user_to_movies_dict, movie_to_genre_dict, movie_to_avg_rating_dict): #ASK if score for this depends on if get_user_genre is correct
    output_dict = {} #dict of movie to average rating.
    users_top_genre = get_user_genre(userID, user_to_movies_dict, movie_to_genre_dict) #user's top genre
    
    list_of_movies_of_genre = []
    
    #gets all movies of users top genre
    for key in movie_to_genre_dict: #iterate thru every key
        if movie_to_genre_dict[key] == users_top_genre:
            list_of_movies_of_genre.append(key)
            
    
    #remove elements user has rated, leaving those that user has not yet rated
    list_of_movies_rated = user_to_movies_dict[userID] # list of tuples (movie, rating) for user
    list_of_movies_to_remove = []
    for movie in list_of_movies_of_genre:
        for tuples in list_of_movies_rated:
            if movie == tuples[0]:
                list_of_movies_to_remove.append(movie)
    for i in list_of_movies_to_remove:
        list_of_movies_of_genre.remove(i)
        
    #Now that you have all movies from user's top genre that user HASNT rated, get its corresponding avg rating
    sorted_dict_of_list_of_movies_of_genre = {}
    for movie in list_of_movies_of_genre:
        sorted_dict_of_list_of_movies_of_genre[movie] =  movie_to_avg_rating_dict[movie]
    
    sorted_dict_of_list_of_movies_of_genre = sorted(sorted_dict_of_list_of_movies_of_genre.items(), reverse = True, key=lambda movie: movie[1]) #returns sorted list of tuples of key value pairs
        
    
    for i in range(3): #0, 1, 2
        try:
            movie = sorted_dict_of_list_of_movies_of_genre[i][0]
            avg_rating = sorted_dict_of_list_of_movies_of_genre[i][1]
            output_dict[movie] = avg_rating
        except:
            break;
            
    return output_dict



#PROF SAID YOUR CODE WILL BE CALLED ON THE CORRECT FUCTIONS, SO THEY DON'T DEPEND ON EACH OTHER IN TERMS OF GRADING