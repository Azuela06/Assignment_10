import qrcode

playlist = qrcode.make('https://open.spotify.com/playlist/3UgqBpRbf8mFxAQ4JtT6lq?si=01b8fb23967d4c76')

playlist.save('Spotify Recommendations.jpg')
