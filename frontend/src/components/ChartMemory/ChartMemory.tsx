import React from 'react';

export interface ChartMemoryProps {
    className?: string;
    children?: React.ReactNode;
}

export const ChartMemory: React.FC<ChartMemoryProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
