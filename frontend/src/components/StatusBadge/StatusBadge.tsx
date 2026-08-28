import React from 'react';

export interface StatusBadgeProps {
    className?: string;
    children?: React.ReactNode;
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
