import React from 'react';
import Sudoku from './sudoku/Sudoku';
import KeyHandler from './sudoku/KeyHandler';
import TextEntry from './TextEntry';

export default function Home() {

	return (
		<KeyHandler>
			<main className='flex max-h-screen flex-col items-center justify-between'>
				<Sudoku />
				<TextEntry />
			</main>
		</KeyHandler>
	);
}
