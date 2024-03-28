import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Comparison = () => {
    const [players, setPlayers] = useState([]);
    const [selectedPlayer1, setSelectedPlayer1] = useState('');
    const [selectedPlayer2, setSelectedPlayer2] = useState('');

    // Fetch available players from the backend API
    useEffect(() => {
        axios.get('/api/players')
            .then(response => {
                setPlayers(response.data);
            })
            .catch(error => {
                console.error('Error fetching players:', error);
            });
    }, []);

    // Handle player selection
    const handlePlayer1Select = (event) => {
        setSelectedPlayer1(event.target.value);
    };

    const handlePlayer2Select = (event) => {
        setSelectedPlayer2(event.target.value);
    };

    return (
        <div>
            <h2>Comparison</h2>
            <div>
                <label htmlFor="player1Select">Select Player 1:</label>
                <select id="player1Select" value={selectedPlayer1} onChange={handlePlayer1Select}>
                    <option value="">Select a player...</option>
                    {players.map(player => (
                        <option key={player.id} value={player.name}>{player.name}</option>
                    ))}
                </select>
            </div>
            <div>
                <label htmlFor="player2Select">Select Player 2:</label>
                <select id="player2Select" value={selectedPlayer2} onChange={handlePlayer2Select}>
                    <option value="">Select a player...</option>
                    {players.map(player => (
                        <option key={player.id} value={player.name}>{player.name}</option>
                    ))}
                </select>
            </div>
            {/* Add comparison details */}
        </div>
    );
};

export default Comparison;
