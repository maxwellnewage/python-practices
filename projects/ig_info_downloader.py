"""
Descarga información publicada en Instagram.
Basada en https://youtu.be/gDHQF7TFyUY
"""
import instaloader
from instaloader import Instaloader, Profile

l = instaloader.Instaloader()

input_profile = input("Cual es tu perfil?: ")
profile = Profile.from_username(l.context, input_profile)

posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

for post in posts_sorted_by_likes:
    print(f"Titulo: {post.title}")
    print(f"Url: {post.url}")
    print(f"Likes: {post.likes}")
    print(f"Ubicación: {post.location}")
    print("----------------------------")
