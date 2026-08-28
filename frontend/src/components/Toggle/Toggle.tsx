import React from 'react';

export interface ToggleProps {
    className?: string;
    children?: React.ReactNode;
}

export const Toggle: React.FC<ToggleProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
