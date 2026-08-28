import React from 'react';

export interface EmptyStateProps {
    className?: string;
    children?: React.ReactNode;
}

export const EmptyState: React.FC<EmptyStateProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
