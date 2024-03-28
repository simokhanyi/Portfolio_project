import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PlayerDetails = () => {
    const [availablePlayers, setAvailablePlayers] = useState([]);
    const [selectedPlayer, setSelectedPlayer] = useState('');

    // Fetch available players from the backend API
    useEffect(() => {
        axios.get('/api/players/available')
            .then(response => {
                setAvailablePlayers(response.data);
            })
            .catch(error => {
                console.error('Error fetching available players:', error);
            });
    }, []);

    // Handle selection of a player
    const handlePlayerSelection = (event) => {
        setSelectedPlayer(event.target.value);
    };

    return (
        <div>
            {/* Player details */}
            <h2>Player Details</h2>
            <p>Select a player:</p>
            <select value={selectedPlayer} onChange={handlePlayerSelection}>
                <option value="">Select a player</option>
                {availablePlayers.map(player => (
                    <option key={player.id} value={player.id}>{player.name}</option>
                ))}
            </select>
            {selectedPlayer && (
                <div>
                    {/* Display details of the selected player */}
                    <p>Name: {selectedPlayer.name}</p>
                    <p>Team: {selectedPlayer.team}</p>
                    <p>Country: {selectedPlayer.country}</p>
                    {/* Add more player details as needed */}
                </div>
            )}
        </div>
    );
};
