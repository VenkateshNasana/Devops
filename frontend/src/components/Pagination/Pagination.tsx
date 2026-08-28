import React from 'react';

export interface PaginationProps {
    className?: string;
    children?: React.ReactNode;
}

export const Pagination: React.FC<PaginationProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
