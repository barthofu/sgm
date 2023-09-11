import { ComponentStyleConfig, defineStyleConfig } from '@chakra-ui/react'

const styles: ComponentStyleConfig  = defineStyleConfig({

    baseStyle: {
        field: {
            _placeholder: {
                opacity: 0.5,
                color: 'tertiary',
                fontSize: '0.9em',
            }
        }
    }
})

export default styles