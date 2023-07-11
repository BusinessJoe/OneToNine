interface BoxProps {
    width: number,
};

const Box = (props: BoxProps) => {
    return (
        <polygon points={`0,0 0,${props.width} ${props.width},${props.width} ${props.width},0`} fill="none" stroke="black" strokeWidth={8} />
    )
};

export default Box;