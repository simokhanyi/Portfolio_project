import React, { useState, useEffect } from 'react';

const UserProfile = () => {
    const [userData, setUserData] = useState(null);

    // Simulating fetching user data from an API
    useEffect(() => {
        // Fetch user data from an API endpoint
        // For demonstration purposes, I'm using dummy data
        const fetchUserData = async () => {
            // Simulate API request delay
            await new Promise(resolve => setTimeout(resolve, 1000));

            // Dummy user data
            const dummyUserData = {
                username: 'john_doe',
                email: 'john@example.com',
                fullName: 'John Doe',
                age: 30,
                bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
                profilePicture: 'https://example.com/profile.jpg'
            };

            // Set user data in state
            setUserData(dummyUserData);
        };

        fetchUserData();
    }, []);

    // Render user profile if data is available
    return (
        <div>
            <h2>User Profile</h2>
            {userData && (
                <div>
                    <div>
                        <img src={userData.profilePicture} alt="Profile" />
                    </div>
                    <div>
                        <p>Username: {userData.username}</p>
                        <p>Email: {userData.email}</p>
                        <p>Name: {userData.fullName}</p>
                        <p>Age: {userData.age}</p>
                        <p>Bio: {userData.bio}</p>
                    </div>
                </div>
            )}
            {!userData && <p>Loading user profile...</p>}
        </div>
    );
};

export default UserProfile;
