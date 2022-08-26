<script>
    import svelteLogo from './assets/svelte.svg'
    import Counter from './lib/Counter.svelte'
    import axios from "axios";
    let options = [];
    let url = '';
    const getOptions = async () => {
        let server_url = 'http://127.0.0.1:8000/api/download/'
        let result = await axios({
            url:server_url,
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },data:JSON.stringify({
                url:url
            })
        });

        options = result.data

    }

</script>

<main>
    <h1>bad Ass <br> Superior <br> Youtube Downloader</h1>
    <div>
        <input bind:value={url} type="text" name="url" id="url" class="url-input" autocomplete="off">
    </div>


    <div class="card">
        <button on:click={getOptions}>download</button>
    </div>
    <div class="table100">
        <table>
            <thead>
            <tr class="table100-head">
                <th class="column1">quality</th>
                <th class="column2">download</th>

            </tr>
            </thead>
            <tbody>

            {#each options as option}
                <tr>
                    <td class="column1">{option.mime_type} {option.resolution}</td>
                    <td class="column2">
                        <a href={option.url}>
                            <button>download</button>
                        </a>
                    </td>

                </tr>
            {:else}

            {/each}

            </tbody>
        </table>
    </div>

</main>

<style>
    .logo {
        height: 6em;
        padding: 1.5em;
        will-change: filter;
    }

    .logo:hover {
        filter: drop-shadow(0 0 2em #646cffaa);
    }

    .logo.svelte:hover {
        filter: drop-shadow(0 0 2em #ff3e00aa);
    }

    .read-the-docs {
        color: #888;
    }

    .url-input {
        width: 100%;
        height: 20px;

    }

    table {
        border-spacing: 1px;
        border-collapse: collapse;
        background: white;
        border-radius: 10px;
        overflow: hidden;
        width: 100%;
        margin: 0 auto;
        position: relative;
    }

    table thead tr {
        height: 60px;
        background: #36304a;

    }

    .table100-head th {
        font-size: 18px;
        color: #fff;
        line-height: 1.2;
        font-weight: unset;
    }

    .column1 {
        width: 260px;
        padding-left: 40px;
    }

    .column2 {
        width: 160px;
    }

    tr {
        color: #212121;
    }

    table {
        direction: ltr;
    }
</style>
