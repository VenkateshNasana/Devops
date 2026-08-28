import React from 'react';

export interface SelectProps {
    className?: string;
    children?: React.ReactNode;
}

export const Select: React.FC<SelectProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
