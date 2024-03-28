import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TeamSearchForm = () => {
    const [teams, setTeams] = useState([]);
    const [selectedTeam, setSelectedTeam] = useState('');

    // Fetch available teams from the backend API
    useEffect(() => {
        axios.get('/api/teams')
            .then(response => {
                setTeams(response.data);
            })
            .catch(error => {
                console.error('Error fetching teams:', error);
            });
    }, []);

    // Handle team selection
    const handleTeamSelect = (event) => {
        setSelectedTeam(event.target.value);
    };

    return (
        <div>
            {/* Team search form */}
            <form>
                <label htmlFor="teamSelect">Select Team:</label>
                <select id="teamSelect" value={selectedTeam} onChange={handleTeamSelect}>
                    <option value="">Select a team...</option>
                    {teams.map(team => (
                        <option key={team.id} value={team.name}>{team.name}</option>
                    ))}
                </select>
                <button type="submit">Search</button>
            </form>
        </div>
    );
};

export default TeamSearchForm;
