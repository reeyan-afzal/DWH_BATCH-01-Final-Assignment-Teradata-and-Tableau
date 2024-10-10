import csv
import json
import ast

def csv_to_json(csv_file_path, json_file_path):
    data = {}

    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            app_id = row['AppID']
            try:
                tags = ast.literal_eval(row["tags"]) if row["tags"] else {}
            except (ValueError, SyntaxError):
                tags = {}

            data[app_id] = {
                "name": row["name"].encode('utf-8').decode('utf-8'),
                "release_date": row["release_date"],
                "required_age": int(row["required_age"]),
                "price": float(row["price"]) if row["price"] else 0.0,
                "dlc_count": int(row["dlc_count"]),
                "detailed_description": row.get("detailed_description", "").encode('utf-8').decode('utf-8'),
                "about_the_game": row.get("about_the_game", "").encode('utf-8').decode('utf-8'),
                "short_description": row.get("short_description", "").encode('utf-8').decode('utf-8'),
                "reviews": row.get("reviews", "").encode('utf-8').decode('utf-8'),
                "header_image": row.get("header_image", ""),
                "website": row.get("website", ""),
                "support_url": row.get("support_url", ""),
                "support_email": row.get("support_email", ""),
                "windows": row["windows"].lower() == "true",
                "mac": row["mac"].lower() == "true",
                "linux": row["linux"].lower() == "true",
                "metacritic_score": int(row["metacritic_score"]) if row["metacritic_score"] else 0,
                "metacritic_url": row.get("metacritic_url", ""),
                "achievements": int(row["achievements"]),
                "recommendations": int(row["recommendations"]),
                "notes": row.get("notes", ""),
                "supported_languages": row.get("supported_languages", "").split(', '),
                "full_audio_languages": row.get("full_audio_languages", "").split(', '),
                "developers": row.get("developers", "").split(', '),
                "publishers": row.get("publishers", "").split(', '),
                "categories": row.get("categories", "").split(', '),
                "genres": row.get("genres", "").split(', '),
                "screenshots": row.get("screenshots", "").split(', '),
                "movies": row.get("movies", "").split(', '),
                "user_score": int(row["user_score"]) if row["user_score"] else 0,
                "positive": int(row["positive"]),
                "negative": int(row["negative"]),
                "estimated_owners": row["estimated_owners"],
                "average_playtime_forever": int(row["average_playtime_forever"]),
                "average_playtime_2weeks": int(row["average_playtime_2weeks"]),
                "peak_ccu": int(row["peak_ccu"]),
                "tags": tags
            }

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

csv_file_path = 'games.csv'
json_file_path = 'games.json'
csv_to_json(csv_file_path, json_file_path)
