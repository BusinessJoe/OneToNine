'use client'

import React, { FormEvent, useEffect, useState } from 'react'
import useWebSocket, { ReadyState } from 'react-use-websocket';

const TextEntry = () => {
    const { sendMessage, lastMessage, readyState } = useWebSocket('ws://localhost:8000/ws');

    const connectionStatus = {
        [ReadyState.CONNECTING]: 'Connecting',
        [ReadyState.OPEN]: 'Open',
        [ReadyState.CLOSING]: 'Closing',
        [ReadyState.CLOSED]: 'Closed',
        [ReadyState.UNINSTANTIATED]: 'Uninstantiated',
    }[readyState];

    const [text, setText] = useState('');

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setText(event.target.value);
    }

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        console.log(text);
        sendMessage(text);
        setText('');
    };

    useEffect(() => {
        if (lastMessage !== null) {
            console.log(lastMessage);
        }
    }, [lastMessage])

    return (
        <form onSubmit={handleSubmit}>
            <div>
                {connectionStatus}
            </div>
            <input type='text' value={text} onChange={handleChange}></input>
        </form>
    )
};

export default TextEntry;