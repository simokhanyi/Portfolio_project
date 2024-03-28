import React from 'react';

const TeamSearchPage = () => {
    // Implement your team search page here
    return (
        <div>
            <h2>Team Search</h2>
            <form>
                <label htmlFor="teamSearch">Search Teams:</label>
                <input type="text" id="teamSearch" name="teamSearch" placeholder="Enter team name" /> 
                <button type="submit">Search</button>
            </form>
            {/* Display search results here */}
        </div>
    );
};

export default TeamSearchPage;
