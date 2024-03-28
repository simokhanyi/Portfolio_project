import React, { useState } from 'react';

const PasswordResetForm = () => {
    const [email, setEmail] = useState('');

    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        // Add logic to send password reset email
        console.log('Password reset email sent to:', email);
        // Reset email field after submission
        setEmail('');
    };

    return (
        <div>
            {/* Password reset form */}
            <h2>Password Reset</h2>
            <form onSubmit={handleSubmit}>
                <label htmlFor="email">Email:</label>
                <input
                    type="email"
                    id="email"
                    name="email"
                    value={email}
                    onChange={handleEmailChange}
                    placeholder="Enter your email"
                    required
                />
                <button type="submit">Reset Password</button>
            </form>
        </div>
    );
};

export default PasswordResetForm;
