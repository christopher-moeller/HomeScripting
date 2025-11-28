import {type ReactNode} from "react";
import {Outlet} from "react-router-dom";

interface LayoutProps {
    children?: ReactNode;
}

export default function Layout({ children }: Readonly<LayoutProps>) {
    return (
        <div>
            <h3>Layout</h3>
            <main>
                {children || <Outlet />}
            </main>
        </div>
    );
};