import { Box, Progress } from '@chakra-ui/react'
import { AffaireDetails, useApiAffairesList } from '@sgm/openapi'
import { Table, createMeta, usePagination } from '@sgm/ui'
import { createColumnHelper } from '@tanstack/react-table'
import React from 'react'
import { DashboardLayout } from '../../components/layouts'
import { FichesTable } from '../../components/modules'

const columnHelper = createColumnHelper<AffaireDetails>()

const columns = [
    columnHelper.accessor('num_affaire', {
        id: 'numero',
        header: 'Numéro',
        meta: createMeta({
            editable: false,
        //     // customValidation: (value) => value < 1000 ? Err('Le numéro d\'affaire doit être supérieur à 1000') : Ok(true)
        })
    }),
    columnHelper.accessor('description', {
        id: 'description',
        header: 'Description',
        meta: createMeta({
            editable: true,
            type: 'text'
        })
    }),
    columnHelper.accessor('avancement_affaire', {
        id: 'avancement',
        header: 'Avancement',
        cell: value => <Box>
            <Box as='span' fontSize='xs'>{value.getValue()}%</Box>
            <Progress value={value.getValue()} 
                background='#c7d2fe'
                borderRadius='10px'
                size='sm'
                mt='.5em'
            />
        </Box>,
    }),
    columnHelper.accessor('client', {
        id: 'client',
        header: 'Client',
        meta: createMeta({
            editable: true,
            type: 'text'
        })
    }),
    columnHelper.accessor(row => row.charge_affaire_detail ? `${row.charge_affaire_detail.prenom} ${row.charge_affaire_detail.nom}` : null, {
        id: 'charge_affaire',
        header: 'Chargé d\'affaire',
    }),
    // TODO: accessor sur la date de création (c'est quelle key ??)
    columnHelper.accessor('date_rendu', { // TODO: date_rendu ou date_cloture ?
        id: 'delais',
        header: 'Délais',
        meta: createMeta({
            editable: true,
            type: 'date'
        })
    }),
    columnHelper.accessor('statut', {
        id: 'statut',
        header: 'Statut',
        meta: createMeta({
            editable: true,
            type: 'select',
            choices: [
                'S00',
                'A00',
                'EHA',
                'EAA',
                'EAC',
                'P00',
                'T00',
                'E00',
                'ECC',
                'INT',
                'ECA',
                'ED',
                'D00',
                'G00',
                'SV0',
                'EST',
                'ECH',
            ]
        }),
    })
]


const AffairesPage: React.FC = () => {

    const { pagination, setPagination, fetchDataOptions } = usePagination()

    const { data } = useApiAffairesList(fetchDataOptions)

	return <>
    	<DashboardLayout 
			title="Affaires"
            removePadding={true}
		>
                <Table<AffaireDetails>
                    title="Liste affaires"
                    columns={columns}
                    data={data}
                    pagination={pagination}
                    setPagination={setPagination}
                    editable={true}
                    rowCanExpand={true}
                    renderSubComponent={({ row }) => <FichesTable affaireId={row.original.id} />}
                    styling={{
                        table: {
                            variant: 'simple'
                        }
                    }}
                    // rowSelectionActionsComponent=
                    
                />
        </DashboardLayout>
    </>
}

export default AffairesPage