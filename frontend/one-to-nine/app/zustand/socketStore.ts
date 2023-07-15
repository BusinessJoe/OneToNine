import { create } from "zustand"

type SocketState = {
    ws_url: string | undefined,
}

type SocketActions = {
    setWsUrl: (ws_url: string) => void,
}

export const useSocketStore = create<SocketState & SocketActions>((set) => ({
    ws_url: undefined,

    setWsUrl: (ws_url: string) => set(() => ({ ws_url }))
}));