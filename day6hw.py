total_views = 0
total_trending = 0
blog_views = [150,800,2500,600,1200,450,3000]
for x in blog_views:
    if x > 1000:
        print(f"{x}views = Trending")
        total_trending += 1
    elif x > 500 and x < 1000:
        print(f"{x}views = Average")
    else:
        print(f"{x}views = Low Traffic")
    total_views += x

print(f"Total views = {total_views}")
print(f"{total_trending} Posts are trendings")


