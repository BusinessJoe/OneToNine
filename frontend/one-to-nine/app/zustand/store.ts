import { create } from "zustand";
import { immer } from 'zustand/middleware/immer';

type SudokuState = {
    fixedValues: (number | undefined)[][],
    userValues: (number | undefined)[][],
    variantData: {},
    selectedCell: [number, number] | undefined,
}

type SudokuActions = {
    setSelectedCell: (selectedCell: [number, number] | undefined) => void,
    setCellValue: (row: number, col: number, value: number | undefined) => void
}

type SudokuSelector<T> = (state: SudokuState) => T

// Log every time state is changed
const log = (config) => (set, get, api) => config(args => {
    console.log("  applying", args)
    set(args)
    console.log("  new state", get())
}, get, api)

export const useSudokuStore = create<SudokuState & SudokuActions>(log(immer<SudokuState & SudokuActions>((set) => ({
    fixedValues: Array.from({ length: 9 }, () => Array.from({ length: 9 }, () => undefined)),
    userValues: Array.from({ length: 9 }, () => Array.from({ length: 9 }, () => undefined)),
    variantData: {},
    selectedCell: [3, 2],
    setSelectedCell: (selectedCell: [number, number] | undefined) => set((state) => {
        state.selectedCell = selectedCell
    }),
    setCellValue: (row: number, col: number, value: number | undefined) => set((state) => {
        state.userValues[row][col] = value
    }),
}))));

enum CellValueState {
    Fixed = "fixed",
    User = "user",
    Error = "error",
}

export const selectCellValue = (row: number, col: number): SudokuSelector<[number, CellValueState] | undefined> => {
    return (state) => {
        const fixed = state.fixedValues[row]?.[col];
        if (fixed !== undefined) {
            return [fixed, CellValueState.Fixed];
        }
        const user = state.userValues[row]?.[col];
        if (user !== undefined) {
            return [user, CellValueState.User]
        }

        return undefined
    }
}