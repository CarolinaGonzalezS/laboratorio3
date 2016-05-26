using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class _Default : System.Web.UI.Page
{
    static List<ClsProducto> lstproductos = new List<ClsProducto>();
    protected void Page_Load(object sender, EventArgs e)
    {
        
        listarProducto();
    }
    protected void btninsertar_Click(object sender, EventArgs e)
    {
        ClsProducto objproducto = new ClsProducto(txtnombre.Text, txturl.Text);
        lstproductos.Add(objproducto);
        listarProducto();
    }

    public void listarProducto() {
        mostrarprod.InnerHtml = " ";
        String lista = "";
        foreach (ClsProducto producto in lstproductos)
        {
            lista = lista + producto.imprimir();
        }
        mostrarprod.InnerHtml = lista;
        grvproducto.DataSource = lstproductos;
        grvproducto.DataBind();
        if (grvproducto.HeaderRow != null && grvproducto.HeaderRow.Cells.Count > 0)
        {
            grvproducto.HeaderRow.Cells[1].Visible = false;
            
        }
        foreach (GridViewRow row in grvproducto.Rows)
        {
            row.Cells[1].Visible = false;
            
        }
    }
    protected void btnmostrar_Click(object sender, ImageClickEventArgs e)
    {
        Session.Add("Productos", lstproductos);
        Server.Transfer("lista.aspx");
    }
}