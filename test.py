import streamlit as st
import googleapiclient.discovery
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Set up API credentials
api_key = 'AIzaSyAp1ItuVi_KDcuYhfeq0WLGeGud4Thc9eU'
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)


def download_song_by_link(yt_link):
    
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the website
    driver.get("https://ytmp3s.nu/evvr/")

    # Find the input tag with id='url'
    input_tag = driver.find_element(By.ID, "url")
    
    # Fill in the input tag with a value
    input_tag.send_keys(yt_link)
    sub=driver.find_element(By.XPATH,'/html/body/form/div[2]/input[2]')
    sub.click()

    down=driver.find_element(By.XPATH,'/html/body/form/div[2]/a[1]')
    down.click()

    time.sleep(150)
    driver.quit()






# Define a function to search for videos
def search_videos(query):
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet'
    ).execute()
    st.write("searched on youtube")
    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('https://www.youtube.com/watch?v=' + search_result['id']['videoId'])

    selected_video = None

    for i, link in enumerate(videos):
        st.video(link)
        button_label = f'Download'    
        st.button(button_label, on_click=download_song_by_link, args=(link,),key=i)
        
    
    
    
        
        
        
        
        







def main():
    st.title("Download Songs")
    # Get user input for search query
    query = st.text_input("Enter keywords to search for videos:")
    #st.button("Search")
    if st.button("Search",key='yt search'):
        search_videos(query)
    
    
if __name__ == "__main__":
    main()