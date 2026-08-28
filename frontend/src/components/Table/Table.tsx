import React from 'react';

export interface TableProps {
    className?: string;
    children?: React.ReactNode;
}

export const Table: React.FC<TableProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
