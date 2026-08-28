import React from 'react';

export interface NavbarProps {
    className?: string;
    children?: React.ReactNode;
}

export const Navbar: React.FC<NavbarProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
