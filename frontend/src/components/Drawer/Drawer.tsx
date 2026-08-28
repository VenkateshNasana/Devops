import React from 'react';

export interface DrawerProps {
    className?: string;
    children?: React.ReactNode;
}

export const Drawer: React.FC<DrawerProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
