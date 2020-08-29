# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import csv


# head 작성
with open(f'./movies_genre.csv', 'a', encoding='utf-8', newline='') as writer_csv:
    field_name_list =['movie_code', 'movie_genre']
    writer = csv.DictWriter(writer_csv, fieldnames=field_name_list)  
    writer.writeheader()


final_movie_data = []

#4
for j in range(1, 6):

    response = requests.get('https://movie.naver.com/movie/bi/ci/filmo.nhn?code=5014&page='+str(j))
    soup = BeautifulSoup(response.text, 'html.parser')

    movies_list = soup.select(
        '#old_content > .table_type_11')
 
    # a_tag = movies_list[0].select('a.title')[1]
    # print(a_tag)

    for i in range(0, len(movies_list[0].select('a.title')), 1):
        a_tag = movies_list[0].select('a.title')[i]
        movie_title = a_tag.contents[0]
        # print(movie_title)
        movie_code = a_tag['href'].split('code=')[1]
        # print(movie_code)
        
        movie_data = {
            'title': movie_title,
            'code': movie_code
        }

        final_movie_data.append(movie_data)
#print(final_movie_data)


#3
for j in range(1, 5):

    response = requests.get('https://movie.naver.com/movie/bi/ci/filmo.nhn?code=4858&page='+str(j))
    soup = BeautifulSoup(response.text, 'html.parser')

    movies_list = soup.select(
        '#old_content > .table_type_11')

    # a_tag = movies_list[0].select('a.title')[1]
    # print(a_tag)

    for i in range(0, len(movies_list[0].select('a.title')), 1):
        a_tag = movies_list[0].select('a.title')[i]
        movie_title = a_tag.contents[0]
        # print(movie_title)
        movie_code = a_tag['href'].split('code=')[1]
        # print(movie_code)
        
        movie_data = {
            'title': movie_title,
            'code': movie_code
        }

        final_movie_data.append(movie_data)


#2 & 1
base_url = "https://movie.naver.com/movie/bi/ci/filmo.nhn?code="
change_url_list=[3212, 1946]

for i in change_url_list:
    url = base_url + str(i)

    #print(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies_list = soup.select(
        '#old_content > .table_type_11')

    # a_tag = movies_list[0].select('a.title')[1]
    # print(a_tag)

    for i in range(0, len(movies_list[0].select('a.title')), 1):
        a_tag = movies_list[0].select('a.title')[i]
        movie_title = a_tag.contents[0]
        # print(movie_title)
        movie_code = a_tag['href'].split('code=')[1]
        # print(movie_code)
        
        movie_data = {
            'title': movie_title,
            'code': movie_code
        }

        final_movie_data.append(movie_data)
# print(final_movie_data)

# 영화 코드, 리뷰
final_movie_data_reple=[]
for movie in final_movie_data:
    movie_code = movie['code']

    # i 값 지정!
    for i in range(1, 11 , 1):        
        params = (
            ('code', movie_code),
            ('type', 'after'),
            ('isActualPointWriteExecute', 'false'),
            ('isMileageSubscriptionAlready', 'false'),
            ('isMileageSubscriptionReject', 'false'),
            ('page', i),
        )

        response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn',  params=params)

        soup = BeautifulSoup(response.text, 'html.parser')

        reveiw_list = soup.select('body > div > div > div.score_result > ul > li')

        count = 0

        for review in reveiw_list:
            #score = review.select_one('div.star_score > em').text
            reple = ''

            # 일반적인 경우
            review_tag = review.select_one(f'div.score_reple > p >span#_filtered_ment_{count}> span#_unfold_ment{count}')
            if review_tag is None:
                reple = review.select_one(f'div.score_reple > p > span#_filtered_ment_{count}').text.strip()

            # 리뷰가 긴 경우
            elif review_tag:
                reple = review.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span > a')['data-src']

            # print(movie_code, reple)

            reple_data = {
                'code': movie_code,
                'reple': reple,
            }
            count +=1


            final_movie_data_reple.append(reple_data)

    # print(final_movie_data_reple)     


for movie in final_movie_data:
    movie_code = movie['code']
    print(movie_code)
    url = ('https://movie.naver.com/movie/bi/mi/basic.nhn?code='+movie_code)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies_genre = soup.select(
        '#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')

    movie_genre = []
    final_movie_data_genre={
        'movie_code': movie_code,
        'movie_genre': movie_genre,
    }
    
    for genre in movies_genre:
        movie_genre.append(genre.get_text())
    
    final_movie_data_genre['movie_genre']=movie_genre

    print(movie_code, final_movie_data_genre)

    # genre_data = {
    #     'movie_code': movie_code,
    #     'movie_genre': final_movie_data_genre,
    # }

#print(final_movie_data_genre)

# csv 파일에 저장
with open(f'./movies_genre.csv', 'a', encoding='utf-8', newline='') as writer_csv:
    field_name_list =['movie_code', 'movie_genre']
    writer = csv.DictWriter(writer_csv, fieldnames=field_name_list)  
    for i in range(0, len(final_movie_data_genre['movie_genre'])):
        writer.writerow(final_movie_data_genre)




# #csv만들기
# field_name_list =['title', 'code']
# with open('movies_title.csv', 'w', encoding='euc-kr', newline='') as writer_csv:
#     writer = csv.DictWriter(writer_csv, fieldnames=field_name_list)  
#     # writer.writeheader()
#     for i in range(0, len(final_movie_data)):
#         writer.writerow(final_movie_data[i])
#     # print(final_movie_data)

# field_name_list =['code', 'reple']
# with open('movies_reple.csv', 'w', encoding='utf-8', newline='') as writer_csv:
#     writer = csv.DictWriter(writer_csv, fieldnames=field_name_list)  
#     # writer.writeheader()
#     for i in range(0, len(final_movie_data_reple)):
#         writer.writerow(final_movie_data_reple[i])

#------






