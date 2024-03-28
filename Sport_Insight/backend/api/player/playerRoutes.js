cont express = require('express');
const mysql = require('mysql');

const app = express();
const port = 3000;

// Create a MySQL connection
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'M!sasa12',
  database: 'SportInsight'
});

// Connect to the database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to database:', err);
    return;
  }
  console.log('Connected to database');
});

// API endpoint to fetch player details by player name
app.get('/players/:player_name', (req, res) => {
  const playerName = req.params.player_name;

  // Query the database to fetch player details
  const query = `SELECT * FROM Players WHERE player_name = ?`;
  connection.query(query, [playerName], (err, results) => {
    if (err) {
      console.error('Error fetching player details:', err);
      res.status(500).json({ error: 'Internal server error' });
      return;
    }

    if (results.length === 0) {
      res.status(404).json({ error: 'Player not found' });
      return;
    }

    const playerDetails = results[0];
    res.json(playerDetails);
  });
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
