import React from 'react';

export interface CheckboxProps {
    className?: string;
    children?: React.ReactNode;
}

export const Checkbox: React.FC<CheckboxProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
