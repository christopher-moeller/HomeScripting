import { createBrowserRouter } from "react-router-dom";
import ScriptOverviewPage from "../pages/ScriptOverviewPage";
import Layout from "../pages/Layout";

export function createAppRouter() {
    return createBrowserRouter([
        {
            path: "/",
            element: <Layout />,
            children: [
                { index: true, element: <ScriptOverviewPage /> }
            ],
        },
    ]);
}