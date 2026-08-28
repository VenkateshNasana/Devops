import React from 'react';

export interface ConfirmationDialogProps {
    className?: string;
    children?: React.ReactNode;
}

export const ConfirmationDialog: React.FC<ConfirmationDialogProps> = ({ className = '', children }) => {
    return (
        <div className={`base-style ${className}`}>
            {children}
        </div>
    );
};
