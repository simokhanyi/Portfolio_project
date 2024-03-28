import React, { useState } from 'react';

const ComparisonPage = () => {
    // State variables to store player selections and stats
    const [player1, setPlayer1] = useState('');
    const [player2, setPlayer2] = useState('');
    const [player1Stats, setPlayer1Stats] = useState({});
    const [player2Stats, setPlayer2Stats] = useState({});

    // Function to handle player selection
    const handlePlayerSelect = (event, playerNumber) => {
        const selectedPlayer = event.target.value;
        if (playerNumber === 1) {
            setPlayer1(selectedPlayer);
        } else if (playerNumber === 2) {
            setPlayer2(selectedPlayer);
        }
    };

    // Function to fetch player statistics
    const fetchPlayerStats = async (playerName, playerNumber) => {
        // Replace 'fetchPlayerStatsAPI' with your backend API endpoint to fetch player statistics
        const response = await fetch(`fetchPlayerStatsAPI?playerName=${playerName}`);
        const data = await response.json();
        if (playerNumber === 1) {
            setPlayer1Stats(data);
        } else if (playerNumber === 2) {
            setPlayer2Stats(data);
        }
    };

    // Function to handle comparison logic
    const handleComparison = () => {
        // Implement your comparison logic here
        // For example, you can compare player statistics stored in player1Stats and player2Stats
        console.log('Comparing:', player1, 'and', player2);
        console.log('Player 1 stats:', player1Stats);
        console.log('Player 2 stats:', player2Stats);
    };

    return (
        <div>
            <h2>Comparison Page</h2>
            {/* Player selection dropdowns */}
            <div>
                <label>Player 1:</label>
                <select value={player1} onChange={(e) => { handlePlayerSelect(e, 1); fetchPlayerStats(e.target.value, 1); }}>
                    <option value="">Select Player 1</option>
                    {/* Populate options dynamically based on available players */}
                    <option value="Player1">Player 1</option>
                    <option value="Player2">Player 2</option>
                    {/* Add more options as needed */}
                </select>
            </div>
            <div>
                <label>Player 2:</label>
                <select value={player2} onChange={(e) => { handlePlayerSelect(e, 2); fetchPlayerStats(e.target.value, 2); }}>
                    <option value="">Select Player 2</option>
                    {/* Populate options dynamically based on available players */}
                    <option value="Player1">Player 1</option>
                    <option value="Player2">Player 2</option>
                    {/* Add more options as needed */}
                </select>
            </div>
            {/* Button to trigger comparison */}
            <button onClick={handleComparison}>Compare</button>
        </div>
    );
};

export default ComparisonPage;
