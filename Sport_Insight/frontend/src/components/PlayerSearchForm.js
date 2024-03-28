import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PlayerSearchForm = () => {
    const [players, setPlayers] = useState([]);
    const [selectedPlayer, setSelectedPlayer] = useState('');

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
    const handlePlayerSelect = (event) => {
        setSelectedPlayer(event.target.value);
    };

    return (
        <div>
            <h2>Player Search Form</h2>
            <label htmlFor="playerSelect">Select a Player:</label>
            <select id="playerSelect" value={selectedPlayer} onChange={handlePlayerSelect}>
                <option value="">Select a player...</option>
                {players.map(player => (
                    <option key={player.id} value={player.name}>{player.name}</option>
                ))}
            </select>
            <button onClick={() => console.log('Selected player:', selectedPlayer)}>Search</button>
        </div>
    );
};

export default PlayerSearchForm;
