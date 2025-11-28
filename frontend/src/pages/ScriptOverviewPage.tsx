import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import { Play, Edit, Plus } from "lucide-react";

interface Script {
  id: string;
  filename: string;
}

const ScriptOverviewPage: React.FC = () => {
    const [scripts, setScripts] = useState<Script[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    const onExecuteClick = (scriptId: string) => {
        axios
        .post("/api/scripts/"+scriptId)
    }

    useEffect(() => {
        axios
        .get("/api/scripts")
        .then((res) => {
            setScripts(res.data);
            setLoading(false);
        })
        .catch((err) => {
            setError("Failed to load scripts");
            setLoading(false);
            console.error(err);
        });
    }, []);

    return (
        <div className="flex flex-col items-center justify-start min-h-screen p-8 text-center gap-8 bg-gray-50">
        <div className="w-full max-w-2xl relative">
            <h1 className="text-4xl font-bold mb-2">HomeScripting</h1>
            <p className="text-lg text-gray-600 mb-8">
            Manage and run your smart home scripts from the web.
            </p>

            {/* Add new script */}
            <button className="absolute top-0 right-0 p-2 rounded-xl shadow hover:shadow-md bg-blue-600 text-white hover:bg-blue-700 transition">
            <Plus size={24} />
            </button>

            {/* Loading */}
            {loading && <p>Loading scripts...</p>}

            {/* Error */}
            {error && <p className="text-red-500">{error}</p>}

            {/* Script Cards */}
            {!loading && !error && (
            <div className="flex flex-col gap-4">
                {scripts.map((script) => (
                <div
                    key={script.id}
                    className="flex justify-between items-center bg-white py-4 px-5 rounded-2xl shadow-sm hover:shadow-md transition border"
                >
                    <span className="text-lg font-medium">{script.filename}</span>

                    <div className="flex items-center gap-3">
                    <button className="p-2 rounded-lg hover:bg-gray-100 transition">
                        <Play size={20} onClick={() => onExecuteClick(script.id)}/>
                    </button>
                    <button className="p-2 rounded-lg hover:bg-gray-100 transition">
                        <Edit size={20} />
                    </button>
                    </div>
                </div>
                ))}
            </div>
            )}
        </div>
        </div>
    );
    };

export default ScriptOverviewPage;