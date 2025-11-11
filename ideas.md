# Project Idea
### Summary
Summary: Music Collaboration + Lyrics
Nodes: Artists
Edges: Featured artists

Node's attributes:
- Popularity
- Genres
- Top 10 tracks lyrics and popularity
- Flag to indicate if they appear in some playlist (top 100: boolean, tiktok: boolean)

Research objectives:
- Basis of communities (D-matrix)
- Correlation between popularity on spotify and social media song presence, or vise versa. Also determine if they kept their fame after social media boost(consistency of popularity)
- Correlation between centrality and popularity
- Identify one hit wonders based on ratio of song popularity and artist popularity

### Questions & Answers
"What is the idea?"
- The idea is to create a network graph of music artists and their relationships based on what other people who listen to them also listen to. The goal is to analyze the structure of the music industry and identify key players and trends.

"Why is it interesting?"
- This is interesting because it can reveal hidden connections between artists, show how musical genres influence each other, and help identify emerging trends in the music industry? We also look at their popularity on spotify versus how viral they are on tiktok. Can we identify consistently popular artists versus one hit wonders? Are there any rising stars because they went viral on social media?

"Which datasets did you need to explore the idea?"
- We explore spotify's API to get artist data, related artists, and track popularity. We also use spotify playlists to identify trending songs. For lyrics, we use the Genius API to extract song lyrics for sentiment analysis and thematic exploration.

"How did you download them?"
- ...

### TODO:
Lyrics might have slang and elision of words (wishin' = wishing) make sure to account for that during the sentiment analysis