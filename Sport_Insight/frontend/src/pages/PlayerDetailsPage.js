import React, { useState, useEffect } from 'react';

const PlayerDetailsPage = () => {
    // Define state variables to store player details
    const [playerDetails, setPlayerDetails] = useState(null);
    const playerId = '123'; // Sample player ID

    // Fetch player details from the API
    useEffect(() => {
        const fetchPlayerDetails = async () => {
            try {
                const response = await fetch(`/api/player/details?player_id=${playerId}`);
                if (response.ok) {
                    const data = await response.json();
                    setPlayerDetails(data);
                } else {
                    console.error('Failed to fetch player details:', response.statusText);
                }
            } catch (error) {
                console.error('Error fetching player details:', error);
            }
        };

        fetchPlayerDetails();
    }, [playerId]); // Fetch player details when component mounts or player ID changes

    return (
        <div>
            <h2>Player Details Page</h2>
            {playerDetails ? (
                <div>
                    <h3>{playerDetails.name}</h3>
                    <p>Age: {playerDetails.age}</p>
                    <p>Team: {playerDetails.team}</p>
                    {/* Add more player details here */}
                </div>
            ) : (
                <p>Loading player details...</p>
            )}
        </div>
    );
};

export default PlayerDetailsPage;
