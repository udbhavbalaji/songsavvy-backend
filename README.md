# Spotify Hit Predictor (API Endpoint)

>
> ### Note
>
> The API endpoint is deprecated due to change in Spotify's API. [*View Spotify's Announcement Here*](https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api)
>


**This is the repository for the API endpoint that exposes the model via an API endpoint.**

## Endpoints

*/api/predict/<song_id>*

## Possible Response Types

*Status Code 200:*

Response shape:

```json
{
  "result": {
    "song_id": string,
    "track_name": string,
    "album_name": string,
    "artist": string,
    "image_url": string,
    "song_url": string,
    "result": integer
  }
}
```


*Status Code 400:*

Response shape:

```json
{
  "error": {
    "error": "Song ID not provided."
  }
}
```


*Status Code 500:*

Response shape:

```json
{
  "error": {
    "error": "Spotify Endpoint has been deprecated"
  }
}
```

## References

- **Spotify Documentation:** [https://developer.spotify.com/documentation/web-api](https://developer.spotify.com/documentation/web-api)
- **Spotify Hit Predictor:** [https://github.com/udbhavbalaji/spotify-hit-predictor](https://github.com/udbhavbalaji/spotify-hit-predictor)


