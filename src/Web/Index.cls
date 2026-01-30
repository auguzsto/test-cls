Class Web.Index Extends %CSP.Page
{

ClassMethod OnPage() As %Status
{
    &html<
        <h1>
            Executando em ambiente local, porém compilando no servidor.
            Apenas um teste
        </h1>
    >

    return $$$OK
}

}
