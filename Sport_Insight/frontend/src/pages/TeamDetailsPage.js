import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TeamDetailsPage = () => {
    const [teamDetails, setTeamDetails] = useState(null);

    useEffect(() => {
        // Make a request to your backend API to fetch team details
        const fetchTeamDetails = async () => {
            try {
                const response = await axios.get('/api/team/details?teamName=Mamelodi Sundowns');
                setTeamDetails(response.data);
            } catch (error) {
                console.error('Error fetching team details:', error);
            }
        };

        fetchTeamDetails();
    }, []);

    return (
        <div>
            <h2>Team Details</h2>
            {teamDetails && (
                <div>
                    <h3>{teamDetails.team_name}</h3>
                    <p>Country: {teamDetails.country}</p>
                    <p>Description: {teamDetails.description}</p>
                </div>
            )}
        </div>
    );
};

export default TeamDetailsPage;
