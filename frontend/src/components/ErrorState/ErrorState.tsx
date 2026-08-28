import React from 'react';

export interface ErrorStateProps {
    className?: string;
    children?: React.ReactNode;
}

export const ErrorState: React.FC<ErrorStateProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
