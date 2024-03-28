import React, { useState } from 'react';
import axios from 'axios';

const PlayerSearchForm = () => {
    const [searchQuery, setSearchQuery] = useState('');
    const [searchResults, setSearchResults] = useState([]);

    const handleSearch = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.get(`/api/players/search?query=${searchQuery}`);
            setSearchResults(response.data);
        } catch (error) {
            console.error('Error searching for players:', error);
            // Handle error, e.g., display an error message to the user
        }
    };

    return (
        <div>
            <form onSubmit={handleSearch}>
                <label htmlFor="searchQuery">Search Players:</label>
                <input 
                    type="text" 
                    id="searchQuery" 
                    value={searchQuery} 
                    onChange={(e) => setSearchQuery(e.target.value)} 
                    placeholder="Enter player name or team" 
                />
                <button type="submit">Search</button>
            </form>
            <div>
                {searchResults.map(player => (
                    <div key={player.id}>
                        <p>{player.name} ({player.team})</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default PlayerSearchForm;
