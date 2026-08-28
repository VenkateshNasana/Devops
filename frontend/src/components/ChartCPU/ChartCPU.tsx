import React from 'react';

export interface ChartCPUProps {
    className?: string;
    children?: React.ReactNode;
}

export const ChartCPU: React.FC<ChartCPUProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
