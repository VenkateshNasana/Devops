import React from 'react';

export interface ChartDiskProps {
    className?: string;
    children?: React.ReactNode;
}

export const ChartDisk: React.FC<ChartDiskProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
