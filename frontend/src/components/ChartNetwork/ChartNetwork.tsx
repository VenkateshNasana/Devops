import React from 'react';

export interface ChartNetworkProps {
    className?: string;
    children?: React.ReactNode;
}

export const ChartNetwork: React.FC<ChartNetworkProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
