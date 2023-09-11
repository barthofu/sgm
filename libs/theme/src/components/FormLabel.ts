import { ComponentStyleConfig, defineStyleConfig } from '@chakra-ui/react'

const styles: ComponentStyleConfig  = defineStyleConfig({

    baseStyle: {
        textTransform: 'uppercase',
        fontWeight: 'bold',
        fontSize: '0.8rem',
        color: 'tertiary'
    }
})

export default styles