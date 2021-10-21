//$ types
const CREATE_HISTORY = 'history_store/CREATE_HISTORY';
const READ_HISTORY = 'history_store/READ_HISTORY';
const UPDATE_HISTORY = 'history_store/UPDATE_HISTORY';
const DELETE_HISTORY = 'history_store/DELETE_HISTORY';

//$ action creators
const createHistory = (entry) => ({
    type: CREATE_HISTORY,
    payload: entry
})

const readHistory = (entry) => ({
    type: READ_HISTORY,
    payload: entry
})

const updateHistory = (entry) => ({
    type: UPDATE_HISTORY,
    payload: entry
})

const deleteHistory = () => ({
    type: DELETE_HISTORY
})

//$ thunks
const createHistoryEntry = (entry) => async dispatch => {
    const response = await fetch('/creepycrawler/history', {
        method: 'POST',
        body: JSON.stringify(entry)
    })

    if (response.ok) {
        const newEntry = await response.json();
        dispatch(createHistory(newEntry));
        return newEntry;
    }
}

//$ reducers
