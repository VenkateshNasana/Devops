import React from 'react';

export interface SidebarProps {
    className?: string;
    children?: React.ReactNode;
}

export const Sidebar: React.FC<SidebarProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
